import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  const user = await signUpUser(firstName, lastName);
  let pic;
  try {
    pic = await uploadPhoto(fileName);
  } catch (err) {
    pic = err.toString();
  }
  return [
    { value: user, status: 'fulfilled' },
    { value: pic, status: 'rejected' },
  ];
}
