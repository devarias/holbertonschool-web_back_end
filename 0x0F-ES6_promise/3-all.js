import { uploadPhoto, createUser } from './utils';

export default async function handleProfileSignup() {
  try {
    const user = await createUser();
    const photo = await uploadPhoto();
    console.log(`${photo.body} ${user.firstName} ${user.lastName}`);
  } catch (err) {
    console.log('Signup system offline');
  }
}
